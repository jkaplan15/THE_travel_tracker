import {useState} from 'react'


function Search({search, searchCountry}) {
    return (
        <div className="search-background">
            <input onChange= {searchCountry} className= "search-bar" value={search} placeholder= 'Search'/>
        </div>
    )
}

export default Search


// function searchPlayer(e) {
//     setSearch(e.target.value)
//   }

//   const filterPlayer = players.filter(player => {
//     if (search==="") {
//       return true
//     }
//     return player.name.toLowerCase().includes(search.toLowerCase())
//   })
  