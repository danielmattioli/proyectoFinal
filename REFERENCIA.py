#agregar un dato a la db

def alta_propiedad(request):
    if request.method == "POST":
        db= Propiedad(titular=request.POST['titular'], ubicacion=request.POST['ubicacion'], dimensiones=request.POST['dimensiones'], poseecartel=request.POST['poseecartel'])
        db.save()
        return render(request, "formulario_alta_propiedad.html")

    return render (request, "formulario_alta_propiedad.html")
#carga las ventas realizadas en la db
def alta_venta(request):
    if request.method == "POST":
        datos_formulario = Form_venta(request.POST)
        if datos_formulario.is_valid():
            midata=datos_formulario.cleaned_data
            db= Venta(nombremartillero=midata['nombremartillero'], comprador=midata['comprador'])
            db.save()
        return render(request, "formulario_alta_venta.html")
    return render(request, "formulario_alta_venta.html")


#buscar un dato en la db


    def busca_venta(request):
    return render (request, "formulario_buscar_venta.html")

#realizo la busqueda en la db
def buscar_vent(request):
    if request.method == "POST":
        vendedor= request.POST['venta']
        datos=Venta.objects.filter(nombremartillero__icontains = vendedor)
        return render(request, "resultado_busqueda_ventas.html", {"vendedores": datos})

    return render (request, "resultado_busqueda_ventas.html")