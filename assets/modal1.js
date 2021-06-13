
let confirm = false;
let evento;
btnDelete = document.querySelectorAll('.icon-excluir a')



let buttonNao =  document.querySelectorAll('.modal-button-confirmacao .button-nao')

document.querySelector('.modal-button-confirmacao .button-nao').addEventListener('click', function(evento){
    modalDelete.style.display = 'none';
}) 
document.querySelector('.modal-delete-content .close').addEventListener('click', function(evento){
    modalDelete.style.display = 'none';
}) 




function confirmDelete(evento){
    modalDelete = document.querySelector('.modal-delete')
}
let link = false



if(btnDelete){
    for(let i = 0; i<btnDelete.length; i++){
        let botaoDelete = btnDelete[i];
        btnDelete[i].addEventListener('click', function(evento){
            modalDelete = document.querySelector('.modal-delete')
            modalDelete.style.display = 'flex';

            buttonSim = document.querySelector('.modal-delete .button-sim > a')
            buttonSim.href  = btnDelete[i].href
            evento.preventDefault()
         

        })   
    }

}
