class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def add(self, newProduct):
        id = str(newProduct.id)
        
        if newProduct.img:
            img = newProduct.img
        else:
            img : newProduct.imagen_link

        size = str(newProduct.ancho) + ' x ' + str(newProduct.largo)
        
        if id not in self.carrito.keys():
            self.carrito[id] = {

                'Producto_id' : newProduct.id,
                'Cantidad' : 1,
                'Producto' : newProduct.type,
                'Tamaño' : size,
                'Acumulado' : newProduct.price,
                'img' : img, 
            }
        else:
            self.carrito[id]["Cantidad"] +=1
            self.carrito[id]["Acumulado"] += newProduct.price

        self.save()

    def save(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def delete(self, newProduct):
        id = str(newProduct.id)
        if id in self.carrito:
            del self.carrito[id]
            self.save()

    def sub(self, newProduct):
        id = str(newProduct.id)
        if id in self.carrito.keys():
            self.carrito[id]["Cantidad"] -=1
            self.carrito[id]["Acumulado"] -= newProduct.price
            if self.carrito[id] <= 0:
                self.delete(newProduct)
                self.save()
    
    def clear(self):
        self.session["carrito"] = {}
        self.session.modified = True
        
                

               
        
        
        