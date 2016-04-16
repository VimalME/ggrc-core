# Copyright (C) 2013 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: dan@reciprocitylabs.com
# Maintained By: vraj@reciprocitylabs.com

import factory
import random
from ggrc import db
from ggrc import models


def random_string(prefix=''):
  return '{prefix}{suffix}'.format(
      prefix=prefix,
      suffix=random.randint(0, 9999999999),
  )


class ModelFactory(factory.Factory):
  # modified_by_id = 1

  @classmethod
  def _create(cls, target_class, *args, **kwargs):
    instance = target_class(*args, **kwargs)
    db.session.add(instance)
    db.session.commit()
    return instance


class TitledFactory(factory.Factory):
  title = factory.LazyAttribute(lambda m: random_string('title'))


class DirectiveFactory(ModelFactory, TitledFactory):

  class Meta:
    model = models.Directive


class ControlFactory(ModelFactory, TitledFactory):

  class Meta:
    model = models.Control

  directive = factory.SubFactory(DirectiveFactory)
  kind_id = None
  version = None
  documentation_description = None
  verify_frequency_id = None
  fraud_related = None
  key_control = None
  active = None
  notes = None


class AssessmentFactory(ModelFactory, TitledFactory):

  class Meta:
    model = models.Assessment


class ControlCategoryFactory(ModelFactory):

  class Meta:
    model = models.ControlCategory

  name = factory.LazyAttribute(lambda m: random_string('name'))
  lft = None
  rgt = None
  scope_id = None
  depth = None
  required = None


class CategorizationFactory(ModelFactory):

  class Meta:
    model = models.Categorization

  category = None
  categorizable = None
  category_id = None
  categorizable_id = None
  categorizable_type = None


class ProgramFactory(ModelFactory):

  class Meta:
    model = models.Program

  title = factory.LazyAttribute(lambda _: random_string("program_title"))
  slug = factory.LazyAttribute(lambda _: random_string(""))


class AuditFactory(ModelFactory):

  class Meta:
    model = models.Audit

  title = factory.LazyAttribute(lambda _: random_string("title"))
  slug = factory.LazyAttribute(lambda _: random_string(""))
  status = "Planned"
  program_id = factory.LazyAttribute(lambda _: ProgramFactory().id)


class ContractFactory(ModelFactory):

  class Meta:
    model = models.Contract


class EventFactory(ModelFactory):

  class Meta:
    model = models.Event
  revisions = []


class RelationshipFactory(ModelFactory):

  class Meta:
    model = models.Relationship
  source = None
  destination = None


class RelationshipAttrFactory(ModelFactory):

  class Meta:
    model = models.RelationshipAttr

  relationship_id = None
  attr_name = None
  attr_value = None


class PersonFactory(ModelFactory):

  class Meta:
    model = models.Person
