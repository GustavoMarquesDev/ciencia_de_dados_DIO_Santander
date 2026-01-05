# RELATÓRIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS

Data: 05/01/2026  
Empresa: Abstergo Industries  
Responsável: Gustavo Marques dos Santos

## Introdução

Este relatório apresenta um **projeto fictício de implementação de serviços em nuvem da AWS** na empresa Abstergo Industries, uma empresa do setor farmacêutico que atualmente não utiliza soluções em cloud computing.

O objetivo principal deste projeto é **reduzir custos operacionais imediatos**, substituir parte da infraestrutura física local e melhorar a organização, segurança e disponibilidade dos dados por meio de serviços gerenciados da AWS.

## Descrição do Projeto

O projeto foi dividido em **três etapas**, cada uma utilizando um serviço AWS diferente, escolhido de acordo com sua simplicidade, custo-benefício e facilidade de gerenciamento.

### Etapa 1: Armazenamento de Arquivos

- **Nome da ferramenta:** Amazon S3
- **Foco da ferramenta:** Armazenamento de arquivos em nuvem com baixo custo
- **Descrição do caso de uso:**  
  O Amazon S3 será utilizado para armazenar documentos internos, relatórios, arquivos laboratoriais e backups. Essa solução substitui servidores locais de arquivos, reduzindo gastos com hardware, manutenção e energia elétrica. O serviço oferece alta durabilidade e fácil acesso aos dados.

- **Documentação oficial:**  
  https://docs.aws.amazon.com/pt_br/s3/

### Etapa 2: Processamento e Servidores

- **Nome da ferramenta:** Amazon EC2 com Amazon EBS
- **Foco da ferramenta:** Execução de aplicações e processamento de dados
- **Descrição do caso de uso:**  
  O Amazon EC2 será utilizado para hospedar aplicações internas e processar dados da empresa. Os volumes Amazon EBS serão usados para armazenar dados das aplicações. Essa abordagem elimina a necessidade de servidores físicos, permitindo pagar apenas pelos recursos utilizados.

- **Documentação oficial:**  
  https://docs.aws.amazon.com/pt_br/ec2/  
  https://docs.aws.amazon.com/pt_br/ebs/

### Etapa 3: Banco de Dados

- **Nome da ferramenta:** Amazon RDS (MySQL ou PostgreSQL)
- **Foco da ferramenta:** Banco de dados relacional gerenciado
- **Descrição do caso de uso:**  
  O Amazon RDS será utilizado para armazenar os dados das aplicações corporativas. O serviço automatiza backups, atualizações e oferece alta disponibilidade, reduzindo o esforço de administração e os riscos de falhas.

- **Documentação oficial:**  
  https://docs.aws.amazon.com/pt_br/rds/

## Conclusão

A implementação dos serviços AWS na empresa Abstergo Industries tem como principal benefício a **redução de custos com infraestrutura física**, além de facilitar o gerenciamento dos sistemas de TI.

Com o uso do Amazon S3, EC2 e RDS, a empresa passa a contar com uma infraestrutura mais simples, escalável e segura. Recomenda-se que, após essa implementação inicial, a empresa continue avaliando novas soluções em nuvem para melhorar seus processos e acompanhar o crescimento do negócio.

---

**Assinatura do Responsável pelo Projeto:**

Gustavo Marques dos Santos
