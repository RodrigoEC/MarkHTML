
<html>
        

    <head>
        <meta charset="utf-8">
        <title>/home/rodrigo/cc/meusProjetos/MarkHTML/output.html</title>
    </head>

    
    <body>
        <h1>:clock3: O HoCo</h1>
<h2>:grey_question: O que é o HoCo</h2>
<p align=center>
  <img width=350 src='https://user-images.githubusercontent.com/42751604/130678288-4c854469-6d06-4c23-ba23-c89b1fa7cde0.png'/>
</p>
<p><br/></p>
<div align='center'>
  <p>
  Olá! Bem-vinde ao HoCo. O HoCo é uma plataforma com objetivo de prover (inicialmente) aos alunos da graduação de Ciência da Computação na UFCG <b> uma plataforma onde ele/ela pode salvar e gerenciar as suas horas complementares do curso</b>.
  </p>
</div>

<h2>:dart: Objetivo</h2>
<p>A falta de praticamente qualquer conhecimento sobre horas e atividades complementares do curso é um conhecido de longa data dos alunos da graduação de Ciência da Computação na UFCG e foi pensando nisso que o <em>HoCo</em> nasceu. </p>
<p><strong>O projeto tem como objetivo sanar essa deficiência do curso provendo um lugar onde os alunos além de salvarem suas horas possam ter conhecimento do seu funcionamento e das normas atuais do curso.</strong></p>
<hr />
<h2>:clipboard: Índice</h2>
<ul>
<li><a href="#grey_question-o-que-é-o-hoco">O que é o HoCo</a></li>
<li><a href="#dart-objetivo">Objetivo</a></li>
<li><a href="#clipboard-índice">Índice</a></li>
<li><a href="#gear-pré-requisitos">Pré-requisitos</a></li>
<li><a href="#running-como-executar-o-projeto">Como executar o projeto</a></li>
<li><a href="#handshake-como-contribuir">Como contribuir</a></li>
<li><a href="#pushpin-mantenedores">Mantenedores</a></li>
<li><a href="#pencil2-licença-e-copyright">Licença e Copyright</a></li>
</ul>
<h2>:gear: Pré-requisitos</h2>
<p>Para executar o projeto você precisa ter instalado na sua máquina o <code>docker</code> e <code>docker-compose</code>. Abaixo estão alguns links úteis para a instalação dessas dependências:</p>
<ul>
<li><a href="https://www.hostinger.com.br/tutoriais/install-docker-ubuntu">Link para instalação do docker</a></li>
<li><a href="https://docs.docker.com/compose/install/">Link para instalação do docker compose</a></li>
</ul>
<h2>:running: Como executar o projeto</h2>
<p><strong>Siga os seguintes passos para a execução do projeto:</strong></p>
<ol>
<li>Fazer o <em>clone</em> do projeto e dos seus submodulos de frontend e backend</li>
</ol>
<pre class="bash codehilite"><code class="language-bash">  git clone --recurse-submodules https://github.com/Guardians-DSC/HoCo
</code></pre>

<ol>
<li>Entrar na pasta do projeto</li>
</ol>
<pre class="bash codehilite"><code class="language-bash">  cd HoCo
</code></pre>

<ol>
<li>Copiar variáveis de ambiente que estão dentro do arquivo <code>.env.example</code></li>
</ol>
<pre class="bash codehilite"><code class="language-bash">  cp .env.example .env
</code></pre>

<ol>
<li>Atualizar submodulos do repositório</li>
</ol>
<pre class="bash codehilite"><code class="language-bash">  git submodule update --remote --recursive
</code></pre>

<ol>
<li>Executar o arquivo <code>docker-compose.yml</code> na raiz do projeto</li>
</ol>
<pre class="bash codehilite"><code class="language-bash">  docker-compose up
</code></pre>

<p>⚠️ ATENÇÂO: Se o comando acima acarretou em um erro de permissão, então você precisa criar um grupo docker, para isso veja o link a seguir: <a href="https://docs.docker.com/engine/install/linux-postinstall/">Link para rodar o docker-compose up sem sudo criando um grupo</a></p>
<p>Pronto! Simples assim e você já consegui executar localmente o projeto, caso você esteja executando o projeto e modificar alguma coisa no código o projeto será atualizado automaticamente.</p>
<h2>:handshake: Como contribuir</h2>
<p>Caso você esteja interessada(o)(e) no projeto e queira contribuir para algum dos projetos do HoCo por favor dê uma olhada nas <a href="https://github.com/Guardians-DSC/HoCo/issues"><strong>issues</strong></a> de cada projeto, se você achou uma issue que lhe interessa leia os documentos de <strong><a href="https://github.com/Guardians-DSC/HoCo/blob/main/CODE_OF_CONDUCT.md">Código de conduta</a></strong> e <strong><a href="https://github.com/Guardians-DSC/HoCo/blob/main/CONTRIBUTING.md">Contribuindo</a></strong> para saber mais detalhes.</p>
<p>⚠️ Ainda estamos trabalhando no projeto, caso você queira acompanhar o avanço do repositório dê um estrelinha ⭐ para você não perder as atualizações do rep.</p>
<h2>:pushpin: Mantenedores</h2>
<ul>
<li><a href="https://github.com/claudiodantas">Franciclaudio Dantas</a></li>
<li><a href="https://github.com/GusttaFS">Gustavo Farias</a></li>
<li><a href="https://github.com/LeandraOS">Leandra Oliveira</a></li>
<li><a href="https://github.com/RodrigoEC">Rodrigo Eloy</a></li>
</ul>
<h2>Contribuidores</h2>
<p><a href="https://github.com/Guardians-DSC/HoCo/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Guardians-DSC/HoCo" />
</a></p>
<h2>:pencil2: Licença e Copyright</h2>
<p>MIT © <a href="https://github.com/Guardians-DSC/HoCo/blob/main/LICENSE">Licença</a></p>
<p><br/></p>
<div align=center>
  <p><i>No mais é isso! Obrigado por ler até aqui, espero que vocẽ tenha gostado do projeto!</i></p>
  <img width=400 src='https://user-images.githubusercontent.com/42751604/125959482-99171781-d212-4bc2-af3c-1d0adcf813dd.gif'/>
</div>
    </body>
</html>
    