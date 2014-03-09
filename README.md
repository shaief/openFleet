openFleet
=========

a small django project with the aim of managing a small business cars fleet

## Currently available views

Except from the admin panel the following views are available.

home:
``'/'``.
This view currently shows the available admin options (add classifications, add owners, add cars) and the future renewals - the ones that are less than a week time are in red, less than a month in orange.

Calssification related views:
add/update
``'/add_group/'``
``'/edit_group/<pk>'``

view list of classifications
``'/groups_list'``

view a classification
``'/group/<pk>'``

Owner related views:
add/update
``'/add_owner/'``
``'/edit_owner/<pk>'``

view list of owners
``'/owners_list'``

view an owner
``'/owner/<pk>'``

Car related views:
add/update
``'/add_car/'``
``'/edit_car/<pk>'``

view list of cars
``'/cars_list'``

view a car
``'/car/<pk>'``
