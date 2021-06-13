
let confirm = false;
let evento;
btnDelete = document.querySelectorAll('.icon-excluir a')



console.log(btnDelete.length)

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

/* document.querySelector('.modal-button-confirmacao [value=Sim]').addEventListener('click', function(evento){
    if(link)
        link.click()
}) */

if(btnDelete){
    for(var i = 0; i<btnDelete.length; i++){
        let botaoDelete = btnDelete[i];
        btnDelete[i].addEventListener('click', function(evento){
            modalDelete = document.querySelector('.modal-delete')
            modalDelete.style.display = 'flex';
            evento.preventDefault()
         
         

        })   
    }

}
