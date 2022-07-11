def cleanData(data):
    MSM = {'img':  'No hay imagen para previsualisar','Unknown': 'Desconocido'}
    img = urlImg(data[0], MSM['img'])
    name = [data[1].strip().replace('\n', ' ') if data[1] is not None else MSM['Unknown']]
    author = [data[2].strip().replace('\n', ' ') if data[2] is not None else MSM['Unknown']]
    year = [data[3].strip().replace('\n', ' ') if data[3] is not None else "Año: "+MSM['Unknown']]
    language = [data[4].strip().replace('\n', ' ') if data[4] is not None else "Idioma: "+MSM['Unknown']]
    ext = [data[5].strip().replace('\n', ' ') if data[5] is not None else "Archivo: "+MSM['Unknown']]
    data = [img, name, author, year, language, ext, data[6]]
    return data

def urlImg(d, msm):
    if d != None:
        img = [d.split()[2] if 'cover-not-exists' not in d else msm]
    else:
        img = msm
    return img




