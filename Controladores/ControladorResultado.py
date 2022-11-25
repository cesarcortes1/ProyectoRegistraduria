from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa

class ControladorResultado():

    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        return self.repositorioResultado.findAll()

    """
        Asignacion candidato y mesa a resultado
    """
    def create(self,infoResultado,id_candidato,id_mesa):
        nuevoResultado=Resultado(infoResultado)
        elCandidato=Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa=Mesa(self.repositorioMesa.findById(id_mesa))
        nuevoResultado.candidato=elCandidato
        nuevoResultado.mesa=laMesa
        return self.repositorioResultado.save(nuevoResultado)

    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    """
        Modificación de resultado (candidato y mesa)
    """
    def update(self,id,infoResultado,id_candidato,id_mesa):
        ResultadoActual = Resultado(self.repositorioResultado.findById(id))
        ResultadoActual.ciudad = infoResultado["ciudad"]
        ResultadoActual.localidad = infoResultado["localidad"]
        elCandidato=Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa=Mesa(self.repositorioMesa.findById(id_mesa))
        ResultadoActual.candidato = elCandidato
        ResultadoActual.mesa = laMesa
        return self.repositorioResultado.save(ResultadoActual)

    def delete(self, id):
        return self.repositorioResultado.delete(id)