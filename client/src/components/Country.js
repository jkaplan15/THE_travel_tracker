import {useState, useEffect} from 'react'


function Country({country}){

    const [toggle, setToggle] = useState(false)

    function toggleCard() {
        setToggle(toggle => !toggle)
    }


    return (
        <div className="card">
            <h1>Country # {country.id}: {country.country_name}</h1>
            <img onClick={toggleCard} src={country.country_image} alt={country.country_name}/>
            <p>{country.country_name}</p>
        </div>
    )
}

export default Country

