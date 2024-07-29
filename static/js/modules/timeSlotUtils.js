export function makeTimeSlots(n) {
    let table = document.getElementById("timeslots")
    let hours = 10
    let mins = 30
    for (let i = 0; i < n; i++) {
        if (mins === 60) {
            mins = 0
            hours++
        }
        if (hours === 13) {
            hours = 1
        }

        let row = document.createElement("tr")
        let tdInput = document.createElement("td")
        let times = document.createElement("td")

        let bx = document.createElement("input")
        bx.type = "checkbox"
        const timeId = i
        bx.id = timeId
        const displayedTime = mins === 0 ? `${hours}:0${mins}` : `${hours}:${mins}`
        bx.setAttribute('data-time', displayedTime)
        bx.addEventListener("change", () => {
            if (bx.checked) {
                sessionStorage.setItem("closed" + timeId, bx.dataset.time)
            }
        })
        
        times.textContent = displayedTime

        tdInput.appendChild(bx)
        row.appendChild(tdInput)
        row.appendChild(times)
        table.appendChild(row)

        mins += 15
    }
}

export function submitOpenTimeSlots(n) {

    let availableTimeSlots = []
    for (let i = 0; i < n; i++) {
        const t = document.getElementById(i)
        if (sessionStorage.getItem("closed" + i) !== null) {
            continue
        } else {
            availableTimeSlots.push(t.dataset.time)
        }
    }

    let params = []
    for (let i = 0; i < availableTimeSlots.length; i++) {
        if (i === 0) {
            params.push("slot" + i + "=")
        } else {
            params.push("&slot" + i + "=")
        }
    }

    const len = params.length

    let merged = []
    for (let i = 0; i < len; i++) {
        merged.push(params[i])
        merged.push(encodeURIComponent(availableTimeSlots[i]))
    }

    merged.push(`&length=${len}`)

    let form = document.getElementById('scheduleForm')
    form.action = form.action + "?" + merged.join('')
}

