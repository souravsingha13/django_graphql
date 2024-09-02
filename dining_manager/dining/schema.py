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


# Query to get the data
class Query(graphene.ObjectType):
    consumers = graphene.List(ConsumerType)
    product_categories = graphene.List(ProductCategoryType)
    products = graphene.List(ProductType)

    def resolve_consumers(self, info, **kwargs):
        return Consumer.objects.all()

    def resolve_product_categories(self, info, **kwargs):
        return ProductCatagory.objects.all()

    def resolve_products(self, info, **kwargs):
        return Products.objects.all()


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


class Mutation(graphene.ObjectType):
    create_consumer = CreateConsumer.Field()
    update_consumer = UpdateConsumer.Field()
    delete_consumer = DeleteConsumer.Field()
    create_product_category = CreateProductCatagory.Field()
    update_product_category = UpdateProductCatagory.Field()
    delete_product_category = DeleteProductCatagory.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
