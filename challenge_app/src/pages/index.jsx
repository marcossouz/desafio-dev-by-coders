import styles from '../styles/Transacao.module.css'
import Head from 'next/head'
import Link from 'next/link'
import { useEffect, useState } from 'react'

export default function Home() {
  const [lojas, setLojas] = useState([])
  const [saldo, setSaldo] = useState(0)
  const [transacoes, setTransacoes] = useState([])

  function carregar_lojas() {
    fetch('http://localhost:8000/cnab/?loja=all')
      .then(res => res.json())
      .then(res => {
        setLojas(res.results)
        }
      )
      .catch(error => console.log(error))
  }

  function carregar_transacoes(loja) {
    fetch(`http://localhost:8000/cnab/?loja=${loja}`)
      .then(res => res.json())
      .then(res => {
        setTransacoes(res.results)
        setSaldo(res.saldo)
        }
      )
      .catch(error => console.log(error))
  }

  useEffect(() => {
    carregar_lojas()
  }, [])

  useEffect(() => {
    if (lojas.length > 0) {
      carregar_transacoes(lojas[0].nome_loja)
    }
  }, [lojas])

  return (
    <div>
      <Head>
        <title>Challenge</title>
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter&display=optional"
          rel="stylesheet"
        />
      </Head>
      <div className={styles.container}>
        <div className={styles.title}>Challenge bycoders_ <Link href='importacao'><button>Importar Dados</button></Link></div>
        <div className={styles.loja}>
          <label>LOJA: </label>
          <select onChange={(e) => carregar_transacoes(e.target.value)}>
            {lojas.map((loja, key) => {
              return <option value={loja.nome_loja} key={key}>{loja.nome_loja}</option>
            })}
          </select>
        </div>

        <table className={styles.tableLoja}>
          <tbody>
          <tr>
            <th>CPF: </th>
            <td>{transacoes[0] && transacoes[0].cpf}</td>
          </tr>
          <tr>
            <th>Dono da loja: </th>
            <td>{transacoes[0] && transacoes[0].dono_loja}</td>
          </tr>
          <tr>
            <th>Nome da loja: </th>
            <td>{transacoes[0] && transacoes[0].nome_loja}</td>
          </tr>
          </tbody>
        </table>
        <table className={styles.transacoes}>
          <tbody>
          <tr>
            <th>Tipo</th> 
            <th>Cartão</th>
            <th>Descrição</th>
            <th>Natureza</th>
            <th>Data</th>
            <th>Hora</th>
            <th>Valor</th>
          </tr>
          {transacoes.map((registro, key) => {
            {console.log(registro.transacao.sinal)}
            return (
              <tr key={key} className={`${registro.transacao.sinal === '+' ? styles.positivo : styles.negativo }`}>
                <td>{registro.transacao.tipo}</td>
                <td>{registro.cartao}</td>
                <td>{registro.transacao.descricao}</td>
                <td>{registro.transacao.natureza}</td>
                <td>{registro.data}</td>
                <td>{registro.hora}</td>
                <td>R$ {registro.valor}</td>  
              </tr>
            )
          })}
              <tr>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <th>Saldo:</th>
                <td>R$ {saldo}</td>
              </tr>
          </tbody>
        </table>
      </div>
    </div>
  )
}
