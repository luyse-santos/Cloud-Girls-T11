const alunos = ['João', 'Juliana', 'caio', 'Ana'];
const medias = [10, 8, 7.5, 9];

const lista = [alunos, medias]

function exibeNomeENota(aluno){
    if(lista[0].includes(aluno)){ //includes checa se o dado está no array
        
        const [alunos, medidas] = lista; 
        const indice = alunos.indexOf(aluno); //método indexOff retorna o nº correspondente ao indice
        const mediaAluno = medias[indice];
        console.log(`${aluno} tem média ${mediaAluno}`);
    }
    else{
        console.log('Estudante não existe na lista');
    }
}

exibeNomeENota('Juliana');
exibeNomeENota('Fulaninho'); 
