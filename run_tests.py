import pytest
import coverage

# Iniciar la cobertura de código, especificando el directorio de origen
cov = coverage.Coverage(source=["src/app"])
cov.start()

# Ejecutar las pruebas en el directorio tests
pytest.main(["tests"])

# Detener y guardar los resultados de la cobertura
cov.stop()
cov.save()

# Imprimir el informe de cobertura en la terminal
print("\nCoverage Report:\n")
cov.report()

# Opcional: Guardar el informe de cobertura en un archivo HTML
cov.html_report(directory='cov_html_report')
print("\nHTML version: cov_html_report/index.html")
