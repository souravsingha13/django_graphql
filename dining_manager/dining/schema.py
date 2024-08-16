import graphene
from graphene_django.types import DjangoObjectType
from .models import Consumer,ProductCatagory,Products


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
    
    consumer = graphene.Field(ConsumerType)

    def mutate(self, info, name, email):
        consumer = Consumer(name=name, email=email)
        consumer.save()
        return CreateConsumer(consumer = consumer)
    

class UpdateConsumer(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required = True)
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    consumer = graphene.Field(ConsumerType)

    def mutate(self, info, name, email):
        consumer = Consumer.objects.get(pk = id )
        if name :
            consumer.name = name
        if email :
            consumer.email = email
        consumer.save()

        return UpdateConsumer(consumer = consumer)

class DeleteConsumer(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    consumer = graphene.Field(ConsumerType)

    def mutate(self, info, id):
        consumer = Consumer.objects.get(pk=id)
        consumer.delete()
        return DeleteConsumer(consumer=None)
    
class Mutation(graphene.ObjectType):
    create_consumer = CreateConsumer.Field()
    update_consumer = UpdateConsumer.Field()
    delete_consumer = DeleteConsumer.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)