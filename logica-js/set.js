const nomes = ["Ana", "Clara", "Maria", "Maria", "João", "João", "João"];

const nomesAtualizados = new Set(nomes); //set é um conjunto que armazena dados

const listaNomesAtualizados = [... new Set(nomesAtualizados)]; //transforma o set em um array

console.log(listaNomesAtualizados);
