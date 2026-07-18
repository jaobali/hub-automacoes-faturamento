export async function getDatabaseStatus() {
  const response = await fetch("http://localhost:8000/status")

  if (!response.ok) {
    throw new Error("Erro ao consultar status do banco")
  }

  const data = await response.json()

  return data
}


export default function DBStatus({ data }) {
  return (
    <div>
      <h1>Status do Banco de Dados</h1>

      <p>
        Status da API: {data.status}
      </p>

      <p>
        Banco conectado: {String(data.database.connected)}
      </p>

      <p>
        Resultado do teste SQL: {data.database.query_result}
      </p>
    </div>
  )
}


export async function getServerSideProps() {
  const data = await getDatabaseStatus()

  return {
    props: {
      data,
    },
  }
}