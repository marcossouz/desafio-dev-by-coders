describe('Testes da listagem', () => {
  it('listagem', () => {
    cy.visit('http://localhost:3000/')

    cy.get('label').contains('LOJA:')
    
    cy.get('button').contains('Importar Dados')

    cy.get('select').should('be.visible')

    cy.get('.Transacao_transacoes__Hl6_Q > tbody > :nth-child(1) > :nth-child(1)').contains('Tipo')

  })
  it('importação', () => {
    cy.get('button').click()

    cy.url().should('include', '/importacao')

    cy.get(':nth-child(3) > button').contains('Enviar').should('be.visible')

    cy.get('.Importacao_title__v_eiD').contains('Challenge bycoders_')

    cy.get('input').should('be.visible')
  })
})