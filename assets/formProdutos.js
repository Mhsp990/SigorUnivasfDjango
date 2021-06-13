function form(){
    sucess = document.querySelector('.adicionar-produto .sucesso')
    console.log('pça')
    console.log(sucess)
let form = document.querySelector('#adicionar-produto-form')
    function sendForm(evento){
        evento.preventDefault()
        let data = new FormData(form)
        let ajax = new XMLHttpRequest()
        let token = document.querySelectorAll('#adicionar-produto-form input')[0].value
        ajax.open('POST', form.action)
        ajax.setRequestHeader('X-CSRF-TOKEN', token)
        ajax.onreadystatechange = function(){
            if(ajax.status === 200 && ajax.readyState == 4){
                sucesso = document.querySelector('.adicionar-produto .sucesso')
              
                sucesso.style.display = 'block'
                console.log('cadastrou')
            }else{
                console.log("Produto não cadastrado")
            }
        }
        ajax.send(data)
        form.reset()
    }
    form.addEventListener('submit', sendForm, false)
}
form()