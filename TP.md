### Créer deux classes python, une classe SimpleMath contenant une fonction statique “addition” prenant deux arguments. Et une classe TestSimpleMath qui hérite de unittest.TestCase et contient une fonction de test unitaire.

```
import unittest

class SimpleMath:

    @staticmethod
    def addition(a, b):
        return a + b

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(2, 3)
        self.assertEqual(result, 5)

        result = SimpleMath.addition(-1, 1)
        self.assertEqual(result, 0)

        result = SimpleMath.addition(0, 0)
        self.assertEqual(result, 0)

# Pour lancer le test
if __name__ == '__main__':
    unittest.main()
```

### Pousser votre code sur un nouveau repository Github et avec Github Actions créer un workflow permettant de lancer les tests unitaires de votre application.

.github/workflows/simplemaths-tests.yml

```
name: Run SimpleMath Unit Tests

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Set up Python 3.11
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Run unit tests
      run: |
        python -m unittest Scriptpython
```

### Créer la fonction soustraction et le test associé. Puis, pousser votre commit. Les tests sont effectués automatiquement via la pipeline.

On ajoute la fonction `soustraction`:

```
def soustraction(a, b):
        return a - b
```
Puis ajoute la fonction `test_soustraction`:

```
def test_soustraction(self):
        result = SimpleMath.soustraction(2, 1)
        self.assertEqual(result, 1)

        result = SimpleMath.soustraction(8, 2)
        self.assertEqual(result, 6)

        result = SimpleMath.soustraction(3, 5)
        self.assertEqual(result, -2)
```


### Ajouter une étape de lint (validation statique et syntaxique de votre code source) dans votre workflow. Utiliser pylint.
### Ajouter une étape qui build un conteneur Docker embarquant votre application. La directive CMD de votre Dockerfile doit exécuter les tests unitaires dès le run d’un nouveau conteneur à partir de cette image
