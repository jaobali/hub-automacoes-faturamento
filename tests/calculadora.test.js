test(
    "espero que 1 seja 1",
    () => {
        expect(1).toBe(1)
    }
)

test("API soma", async () => {
    const response = await fetch(
        "http://localhost:8000/somar?a=1&b=2"
    )

    console.log(response)

    const data = await response.json()

    expect(data.resultado).toBe(3)
})