import graphene
from graphene_django.types import DjangoObjectType
from .models import Consumer,ProductCatagory,Products


class CustomerType(DjangoObjectType):
    class Meta:
        model = Consumer

class ProductCatagoryType(DjangoObjectType):
    class Meta:
        model = ProductCatagory

class ProductType(DjangoObjectType):
    class Meta:
        model = Products


# Mutations for CRUD operatons

class CreateConsumer(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
    
    consumer = graphene.Field(CustomerType)

    def mutate(self, info, name, email):
        consumer = Consumer(name=name, email=email)
        consumer.save()
        return CreateConsumer(consumer = consumer)