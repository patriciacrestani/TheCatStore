$(function() {
    $("#btn-msg").click(function(e) { validaMensagemFunction(e) })
    $("#btn-cadastro").click(function(e) { validaCadastroFunction(e) })
    $("#like").text($("#like").data("like"));
    $("#dislike").text($("#dislike").data("dislike"));
})


function validaMensagemFunction(e) {
   e.preventDefault()

   let nome_valido = nomeValidoFunction()
   let email_valido = emailValidoFunction()
   let assunto_valido = assuntoValidoFunction()
   let mensagem_valido = mensagemValidoFunction()

   if (nome_valido && email_valido && assunto_valido && mensagem_valido) {
        $('.toast').toast('show');
   }
}

function nomeValidoFunction() {
   let nome = $("#nome")

   if (nome.val() === '') {
      nome.addClass("is-invalid")
      nome.removeClass("is-valid")
      return false
   }
   else {
      nome.removeClass("is-invalid")
      nome.addClass("is-valid")
      return true
   }
}

function emailValidoFunction() {
   let email = $("#email")

   if (email.val() === '') {
      email.addClass("is-invalid")
      email.removeClass("is-valid")
      return false
   }
   else {
      email.removeClass("is-invalid")
      email.addClass("is-valid")
      return true
   }
}

function assuntoValidoFunction() {
   let assunto = $("#assunto")
   if (assunto.val() === '') {
      assunto.addClass("is-invalid")
      assunto.removeClass("is-valid")
      return false
   }
   else {
      assunto.removeClass("is-invalid")
      assunto.addClass("is-valid")
      return true
   }
}

function mensagemValidoFunction() {
   let mensagem = $("#mensagem")

    if (mensagem.val() === '') {
      mensagem.addClass("is-invalid")
      mensagem.removeClass("is-valid")
      return false
   }
   else {
      mensagem.removeClass("is-invalid")
      mensagem.addClass("is-valid")
      return true
   }
}

function validaCadastroFunction(e) {
   e.preventDefault()

   let nome_valido = nomeValidoFunction()
   let sobrenome_valido = sobrenomeValidoFunction()
   let cpf_valido = cpfValidoFunction()
   let sexo_valido = sexoValidoFunction()
   let estado_valido = estadoValidoFunction()
   let email_valido = emailValidoFunction()
   let senha_valido = senhaValidoFunction()
   let confsenha_valido = confsenhaValidoFunction()
   let termos_valido = notificacoesValidoFunction()
}

function sobrenomeValidoFunction() {
   let sobrenome = $("#sobrenome")

   if (sobrenome.val() === '') {
      sobrenome.addClass("is-invalid")
      sobrenome.removeClass("is-valid")
      return false
   }
   else {
      sobrenome.removeClass("is-invalid")
      sobrenome.addClass("is-valid")
      return true
   }
}

function cpfValidoFunction() {
   let cpf = $("#cpf")

   if (cpf.val() === '') {
      cpf.addClass("is-invalid")
      cpf.removeClass("is-valid")
      return false
   }
   else {
      cpf.removeClass("is-invalid")
      cpf.addClass("is-valid")
      return true
   }
}

function sexoValidoFunction() {
   let feminino = $("#sexo-feminino")
   let masculino = $("#sexo-masculino")
   let outro = $("#sexo-outro")
   let sexo = $("#sexo-feedback")
   let botoes = $("input[name='sexo']:checked")

    if (botoes.length === 0) {
      feminino.addClass("is-invalid")
      feminino.removeClass("is-valid")
      masculino.addClass("is-invalid")
      masculino.removeClass("is-valid")
      outro.addClass("is-invalid")
      outro.removeClass("is-valid")
      sexo.addClass("d-block")
      return false
   }
   else {
      feminino.removeClass("is-invalid")
      feminino.addClass("is-valid")
      masculino.removeClass("is-invalid")
      masculino.addClass("is-valid")
      outro.removeClass("is-invalid")
      outro.addClass("is-valid")
      sexo.removeClass("d-block")
      return true
   }
}

function estadoValidoFunction() {
   let estado = $("#estado")
   if (estado.val() === '') {
      estado.addClass("is-invalid")
      estado.removeClass("is-valid")
      return false
   }
   else {
      estado.removeClass("is-invalid")
      estado.addClass("is-valid")
      return true
   }
}

function senhaValidoFunction() {
   let senha = $("#senha")

   if (senha.val() === '') {
      senha.addClass("is-invalid")
      senha.removeClass("is-valid")
      return false
   }
   else {
      senha.removeClass("is-invalid")
      senha.addClass("is-valid")
      return true
   }
}

function confsenhaValidoFunction() {
   let senha = $("#senha")
   let confsenha = $("#confirmar-senha")

   if (confsenha.val() === senha.val()) {
      if(confsenha.val() === ''){
        confsenha.addClass("is-invalid")
        confsenha.removeClass("is-valid")
        return false
      }
      else{
        confsenha.removeClass("is-invalid")
        confsenha.addClass("is-valid")
        return true
      }
   }
   else {
      confsenha.addClass("is-invalid")
      confsenha.removeClass("is-valid")
      return false
   }
}

function notificacoesValidoFunction() {
   let termos = $("#termos")
   let notificacao = $("#notificacao")
   let notificacoes_feedback = $("#notificacoes-feedback")
   let botoes = $("input[name='notificacao']:checked")

   if (botoes.length === 0) {
      termos.addClass("is-invalid")
      termos.removeClass("is-valid")
      notificacao.addClass("is-invalid")
      notificacao.removeClass("is-valid")
      notificacoes_feedback.addClass("d-block")
      return false
   }
   else {
      termos.removeClass("is-invalid")
      termos.addClass("is-valid")
      notificacao.removeClass("is-invalid")
      notificacao.addClass("is-valid")
      notificacoes_feedback.removeClass("d-block")
      return true
   }
}

$("#like").next().on("click", function () {
    let like = $("#like");
    let dislike = $("#dislike");
    let likes = like.data("like");
    let dislikes = dislike.data("dislike");
    let liked = like.data("liked");
    let disliked = dislike.data("disliked");

    if (liked === "no") {
        like.data("like", likes + 1);
        like.data("liked", "yes");
        if (disliked === "yes") {
            dislike.data("dislike", dislikes - 1)
            dislike.data("disliked", "no");
            $("#dislike-icon").toggleClass("fas");
            $("#dislike-icon").toggleClass("far");
        }
    } else {
        like.data("like", likes - 1);
        like.data("liked", "no")
    }

    $("#like-icon").toggleClass("fas");
    $("#like-icon").toggleClass("far");

    $("#like").text($("#like").data("like"));
    $("#dislike").text($("#dislike").data("dislike"));

    return false;
})

$("#dislike").prev().on("click", function () {
    let like = $("#like");
    let dislike = $("#dislike");
    let likes = like.data("like");
    let dislikes = dislike.data("dislike");
    let liked = like.data("liked");
    let disliked = dislike.data("disliked");
    if (disliked === "no") {
        dislike.data("dislike", dislikes + 1);
        dislike.data("disliked", "yes");
        if (liked === "yes") {
            like.data("like", likes - 1)
            like.data("liked", "no")
            $("#like-icon").toggleClass("fas");
            $("#like-icon").toggleClass("far");
        }
    } else {
       dislike.data("dislike", dislikes - 1);
       dislike.data("disliked", "no")
    }

    $("#dislike-icon").toggleClass("fas");
    $("#dislike-icon").toggleClass("far");

    $("#like").text($("#like").data("like"));
    $("#dislike").text($("#dislike").data("dislike"));

    return false;
})