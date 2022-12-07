import json
with open('./regiones_comunas/regiones_comunas_format.json', encoding="utf8") as f:
    regiones = json.load(f)
    regiones = regiones['regiones']
    
def get_regiones():
    '''
    Parameters:
        None
    Return (list of dict):
        Lista de regiones [{region: 'region', comunas: ['comuna1', 'comuna2', ...]}]'''
    return regiones

def list_regions(regiones):
    '''
    Parameters:
        regiones (list of dict): lista de regiones [{region: 'region', comunas: ['comuna1', 'comuna2', ...]}]
    Return (void)
        Lista con los nombres de las regiones'''
    for r in regiones:
        print(r['region'])

def search_region(region):
    '''
    Parameters:
        region (str): nombre de la región a buscar
    Return (region: [{region: 'region', comunas: ['comuna1','comuna2']}] ) or (None):
        Lista dict con la region y comunas de la región'''
    
    # Buscar región, ejemplo: 'Arica y Parinacota' o 'Arica_y_Parinacota '
    region = region.replace(' ', '_')

    for data_region in regiones:
        if data_region['region'] == region:
            print('Region encontrada')
            return data_region
    print('Region no encontrada')
    return None