import graphene
from graphene_django.types import DjangoObjectType
from .models import Consumer, ProductCatagory, Products, Expenses, Meal


class ConsumerType(DjangoObjectType):
    class Meta:
        model = Consumer


class ProductCategoryType(DjangoObjectType):
    class Meta:
        model = ProductCatagory


class ProductType(DjangoObjectType):
    class Meta:
        model = Products


class MealType(DjangoObjectType):
    class Meta:
        model = Meal


# Query to get the data
class Query(graphene.ObjectType):
    consumers = graphene.List(ConsumerType)
    product_categories = graphene.List(ProductCategoryType)
    products = graphene.List(ProductType)
    meals = graphene.List(MealType)

    def resolve_consumers(self, info, **kwargs):
        return Consumer.objects.all()

    def resolve_product_categories(self, info, **kwargs):
        return ProductCatagory.objects.all()

    def resolve_products(self, info, **kwargs):
        return Products.objects.all()

    def resolve_meals(self, info, **kwargs):
        return Meal.objects.all()


# Mutations for CRUD operatons


class CreateConsumer(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        image = graphene.String(required=True)

    consumer = graphene.Field(ConsumerType)

    def mutate(self, info, name, email, image):
        consumer = Consumer(name=name, email=email, image=image)
        consumer.save()
        return consumer


class UpdateConsumer(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        image = graphene.String(required=True)

    consumer = graphene.Field(ConsumerType)

    def mutate(self, info, name, email, id, image):
        consumer = Consumer.objects.get(pk=id)
        if name:
            consumer.name = name
        if email:
            consumer.email = email
        if image:
            consumer.image = image
        consumer.save()

        return UpdateConsumer(consumer=consumer)


class DeleteConsumer(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    consumer = graphene.Field(ConsumerType)

    def mutate(self, info, id):
        consumer = Consumer.objects.get(pk=id)
        consumer.delete()
        return DeleteConsumer(consumer=None)


class CreateProductCatagory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    product_category = graphene.Field(ProductCategoryType)

    def mutate(self, info, name):
        product_category = ProductCatagory(name=name)
        product_category.save()

        return CreateProductCatagory(product_category=product_category)


class UpdateProductCatagory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)

    product_category = graphene.Field(ProductCategoryType)

    def mutate(self, info, id, name):
        product_category = ProductCatagory.objects.get(pk=id)
        if name:
            product_category.name = name
        product_category.save()

        return CreateProductCatagory(product_category=product_category)


class DeleteProductCatagory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            product_category = ProductCatagory.objects.get(pk=id)
            product_category.delete()

            return DeleteProductCatagory(success=True)

        except ProductCatagory.DoesNotExist:
            return DeleteProductCatagory(success=False)


class CreateMeal(graphene.Mutation):
    class Arguments:
        consumer = graphene.ID(required=True)
        meal_date = graphene.Date(required=True)
        meal_count = graphene.Int(required=True)

    meal = graphene.Field(MealType)

    def mutate(self, info, consumer, meal_date, meal_count):
        consumer = Consumer.objects.get(pk=consumer)
        meal = Meal(consumer=consumer, meal_date=meal_date, meal_count=meal_count)
        meal.save()

        return CreateMeal(meal=meal)


class UpdateMeal(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        consumer = graphene.ID(required=True)
        meal_date = graphene.Date(required=True)
        meal_count = graphene.Int(required=True)

    meal = graphene.Field(MealType)

    def mutate(self, info, consumer, meal_date, meal_count, id):
        meal = Meal.objects.get(id=id)
        consumer = Consumer.objects.get(pk=consumer)
        if consumer:
            meal.consumer = consumer
        if meal_date:
            meal.meal_date = meal_date
        if meal_count:
            meal.meal_count = meal_count
        meal.save()
        return UpdateMeal(meal=meal)


class DeleteMeal(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    meal = graphene.Field(MealType)

    def mutate(self, info, id):
        meal = Meal.objects.get(pk=id)
        if meal:
            meal.delete()


class ProductCreate(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        category_id = graphene.ID(required=True)

    product = graphene.Field(ProductType)

    def mutate(self, info, name, category_id):
        category_id = ProductCatagory.objects.get(pk=category_id)
        product = Products(name=name, catagory=category_id)
        product.save()

        return ProductCreate(product=product)


class ProductUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
        category_id = graphene.ID(required=True)

    product = graphene.Field(ProductType)

    def mutate(self, info, name, category_id, id):
        product = Products.objects.get(pk=id)
        category_id = ProductCatagory.objects.get(pk=category_id)
        if name:
            product.name = name
        if category_id:
            product.catagory = category_id
        product.save()

        return ProductCreate(product=product)


class ProductDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    product = graphene.Field(ProductType)

    def mutate(self, info, id):
        product = Products.objects.get(pk=id)
        product.delete()


class Mutation(graphene.ObjectType):
    create_consumer = CreateConsumer.Field()
    update_consumer = UpdateConsumer.Field()
    delete_consumer = DeleteConsumer.Field()
    create_product_category = CreateProductCatagory.Field()
    update_product_category = UpdateProductCatagory.Field()
    delete_product_category = DeleteProductCatagory.Field()
    create_meal = CreateMeal.Field()
    update_meal = UpdateMeal.Field()
    delete_meal = DeleteMeal.Field()
    product_create = ProductCreate.Field()
    product_update = ProductUpdate.Field()
    product_delete = ProductDelete.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
