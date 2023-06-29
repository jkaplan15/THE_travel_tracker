import Country from './Country'

function CountryList({countries}){

    const countryComponents = countries.map(country => {
        return <Country key={country.id} country={country} />
    })

    return (
        <div className="country-list">{countryComponents}</div>
        )
}

export default CountryList