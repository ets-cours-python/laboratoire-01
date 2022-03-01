import os

def script_test(nom_script, dico_var_val):

  # Constantes
  TABULATION = chr(9)         # Tabulation    (\t)
  NOUVELLE_LIGNE = chr(10)    # Saut de ligne (\n)
  EPS = 0.001                 # Tolérance à l'erreur

  # Indicateur de succès
  succes = True

  # Vérifier que le script existe
  import os
  assert os.path.exists(nom_script), f'Nous n\'avons pas pu ouvrir {nom_script}'

  # Vérifier que les variables sont présentes et/ou ont les bons noms
  var_trouvee = []
  msg_err_1 = NOUVELLE_LIGNE + 'Les variables suivantes n\'ont pas été trouvées : '
  for var in dico_var_val.keys():
    try:
      exec(f'from {nom_script} import {var}')
      var_trouvee.append(True)
    except:
      succes = False
      var_trouvee.append(False)
      msg_err_1.join(f'{NOUVELLE_LIGNE + TABULATION + nom_script}>{var}')

  # Vérifier que les variables présentes ont les bonnes valeurs
  msg_err_2 = NOUVELLE_LIGNE + 'Les tests suivants ont échoué :'
  for var, val, est_trouvee in zip(dico_var_val.keys(), 
                                   dico_var_val.values(), 
                                   var_trouvee):
    if est_trouvee:
      try:
        expression = f'assert {var} == {val}' 
        eval(expression)
      except AssertionError as msg:
          succes = False
          msg_err_2.join(NOUVELLE_LIGNE + TABULATION + expression)

  # Signaler l'échec des tests et retourner les messages d'erreur
  if succes:
     return succes, ''
  else:
    return succes, msg_err_1 + msg_err_2
  
def test_main():
  succes, msg_err = script_test('somme.py', {'a':1, 'b':2, 'c':3})
  assert succes, msg_err
