# -*- coding:utf-8 -*-
#--
# Copyright (c) 2012-2014 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
#--

from elixir import ManyToOne
from elixir import using_options
from nagare.database import session
from elixir import Field, UnicodeText

from kansha.models import Entity


class DataCardDescription(Entity):
    using_options(tablename='card_description')

    description = Field(UnicodeText, default=u'')
    card = ManyToOne('DataCard', ondelete='cascade')

    def copy(self, parent):
        new_data = DataCardDescription(card=parent,
                                       description=self.description)
        session.flush()
        return new_data

    @classmethod
    def get_by_card(cls, card):
        q = cls.query
        q = q.filter_by(card=card)
        return q.first()