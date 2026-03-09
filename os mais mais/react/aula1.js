const express = ('express');
const app = express();
const porta = 3000;

app.get('/'(req, res) => {
 res.send('Servidor do Teerceirão rodando com sucesso!');
});

 app.get('/perfil',(req, res)=>{
    res.send('Olá eu sou a Ray e estou aprendendo back end');
 })
 app.listen(porta, () =>{
   console.log(`servidor aberto em http://locsalhost:${porta}`);
});
junior year