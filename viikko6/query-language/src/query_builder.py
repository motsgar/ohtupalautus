from matchers import All, And, PlaysIn, HasAtLeast, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, stack = All()):
        print(stack)
        self.stack = stack

    def plays_in(self, team):
        return QueryBuilder(And(self.stack, PlaysIn(team)))
    
    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.stack, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.stack, HasFewerThan(value, attr)))
    
    def one_of(self, *matchers):
        return QueryBuilder(And(self.stack, Or(*matchers)))

    def build(self):
        return self.stack