#Enlève le suffixe d'une string
def removesuffix(self, suffix):
    if self.endswith(suffix):
        return self[:-len(suffix)]
    else:
        return self[:]


#Iterateur pour avoir accès à la valeur d'un itérateur et la suivante en même temps 
def doubleIterate(iterable):
    iterator = iter(iterable)
    item = next(iterator, "FIN")

    for next_item in iterator:
        yield item, next_item
        item = next_item

    yield item, None


