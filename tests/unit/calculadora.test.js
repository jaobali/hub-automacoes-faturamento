// Teste com a API
test("API soma", async () => {
    const response = await fetch(
        "http://localhost:8000/somar?a=1&b=2"
    )

    console.log(response)

    const data = await response.json()

    expect(data.resultado).toBe(3)
})