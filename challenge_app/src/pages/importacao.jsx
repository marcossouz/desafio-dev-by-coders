import styles from '../styles/Importacao.module.css'
import Link from 'next/link'
import { useState } from 'react'
import FormData from 'form-data'

export default function Home() {
    const [file, setFile] = useState(null)
    const [msg, setMsg] = useState('')
    const [active, setActive] = useState(false)
    const [status, setStatus] = useState(0)

    const uploadToClient = (event) => {
        if (event.target.files && event.target.files[0]) {
          const i = event.target.files[0];
    
          setFile(i);
        }
      };

    function uploadtoServer() {
        setActive(true)
        const formData = new FormData()
        formData.append('file', file)
        fetch('http://localhost:8000/cnab/', {
           method: 'POST',
            body: formData
        })
        .then(res => res.json())
        .then(json => {
            if(json.status == 400) {
                setMsg('Arquivo enviando mas não foi possível processá-lo, o arquivo enviado está correto?')
                setStatus(400)
            } else {
                setStatus(200)
                setMsg('Arquivo enviando com sucesso. Adicionamos ao banco de dados o você envio de novidade ;)')
            }
            setActive(false)
        })
        .catch(err => {
            console.error(err)
            setStatus(500)
            setActive(false)
            
        })
    }

    return (
      <div className={styles.container}>
        <div className={styles.title}>Challenge bycoders_ <Link href='/'><button>Voltar</button></Link></div>
        <div className={styles.importar}>
            <label>Importar dados CNAB</label>
            <div className={msg ? styles.msg : ''} style={ status == 400 ? {'backgroundColor': '#faa'} : {'backgroundColor': '#2f2'}}>{msg}</div>
            <div>
                <input type='file' onChange={uploadToClient}></input>
                <button onClick={uploadtoServer}>{ active ? 'Enviando...' : 'Enviar'}</button>
            </div>
        </div>
      </div>
    )
  }