class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito 
    
    def agregar(self, producto):
        idProducto = str(producto.idProducto)
        if idProducto not in self.carrito:
            self.carrito[idProducto]={
                "producto_id":producto.idProducto, 
                "nombre": producto.nomProducto,
                "precio":  producto.precio,
                "cantidad": 1,
                "total": producto.precio,
            }
        else:
            self.carrito[idProducto]["cantidad"] += 1
            self.carrito[idProducto]["total"] += producto.precio

            # for key, value in self.carrito.items():
            #     if key==producto.idProducto:
            #         value["cantidad"] = value["cantidad"]+1
            #         value["precio"] = producto.precio
            #         value["total"]= value["total"] + producto.precio
            #         break
        self.guardar_carrito()


    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True

    def eliminar(self, producto):
        idProducto = str(producto.idProducto)
        if idProducto in self.carrito:
            del self.carrito[idProducto]
            self.guardar_carrito()

        # id = producto.idProducto
        # if id in self.carrito: 
        #     del self.carrito[id]
        #     self.guardar_carrito()
    
    def restar (self,producto):
        idProducto = str(producto.idProducto)
        if idProducto in self.carrito:
            self.carrito[idProducto]["cantidad"] -= 1
            self.carrito[idProducto]["total"] -= producto.precio
            if self.carrito[idProducto]["cantidad"] < 1:
                self.eliminar(producto)
            self.guardar_carrito()

        # for key, value in self.carrito.items():
        #     if key == producto.idProducto:
        #         value["cantidad"] = value["cantidad"]-1
        #         value["total"] = int(value["total"])- producto.precio
        #         if value["cantidad"] < 1:   
        #             self.eliminar(producto)
        #         break
        # self.guardar_carrito()
     
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 

    def calcularTotal(self):
        total = 0
        for i in self.carrito():
            if i > 0:
                total =+ self.carrito[i]["total"]
        return total