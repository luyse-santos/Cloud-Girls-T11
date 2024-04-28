const notas = [10, 9.5, 8, 7, 6];


//map é um método callback para achar uma função dentro de outra

/*const notasAtualizadas = notas.map(function(nota){
    
    return nota +1;
})*/

const notasAtualizadas = notas.map((nota) => nota + 1 >= 10 ? 10: nota + 1);

//nota +1 é o retorno, se nota + 1  > = 10 retorna 10 (? 10), se nao (: ) retorna +1

//O forEach() não retorna nada,
console.log(notasAtualizadas);