=============================
Django Hit Count Mixed Object
=============================

Allow hit count mixed objects represented into relational database, using NoSQL databases.

Motivation
==========

Imagine that you have ordered items, and each one can be customized with diferent toppings.
Example:

  * Round Pizza with toppings (Spinach, Hot Sopresatta)
  * Round Pizza with toppings (Anchovies, Fried Eggplant)

So you want to know, the number of items ordered with the same toppings.

Application provides the following methods
==========================================

* push_hit

    ``object:`` model instance

    ``related_objects:`` sequence of model instances that compound  the mixed object together the object param

    ``hit_count:`` number of hits to push

* get_hit_count

    ``object:`` model instance

    ``related_objects:`` sequence of model instances that compound  the mixed object together the object param


* get_mixed_objects


      ``filters:`` dictionary of filter to quering mixed objects

      ``limit:`` max number of mixed objects to return

      ``offset:`` skip to this position before returning the results

      ``order_by:`` order the mixed objects by these keys


Feedback
========

If you have questions about usage or development you can send an email to rmaceissoft at gmail dot com
