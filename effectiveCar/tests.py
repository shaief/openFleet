from django.test import TestCase
from effectiveCar.models import Car, Owner
# Create your tests here.


class SimpleTest(TestCase):
    def test_basic_addition(self):
        self.assertEqual(1+1, 2)


class CarTests(TestCase):

    def test_str(self):
        c = Car(license_id='12-345-90', current_owner='Jon Doe')
        self.assertEqual(str(c), '12-345-90 Jon Doe')


from django.test.client import RequestFactory
from effectiveCar.views import CarListView


class CarListViewTests(TestCase):

    def test_no_car_in_context(self):

        factory = RequestFactory()
        request = factory.get('/')

        response = CarListView.as_view()(request)

        self.assertEquals(
            list(response.context_data['object_list']), [],)

    def test_car_in_context(self):

        factory = RequestFactory()
        request = factory.get('/')
        o = Owner.objects.create(name='Neil Young')
        c = Car.objects.create(
            license_id='12-345-67',
            current_owner='Neil Young')

        response = CarListView.as_view()(request)

        self.assertEquals(
            list(response.context_data['object_list']), [c],)
