import '../App.css';
import {useState, useEffect} from 'react'
import { Route, Switch } from "react-router-dom"

import NavBar from './NavBar'
import Header from './Header'
import CountryList from './CountryList'
import NewTripForm from './NewTripForm'
import UpdateTripForm from './UpdateTripForm'
import Search from './Search'


function App() {

  const [countries, setCountries] = useState([])
  const [trips, setTrips] = useState([])
  const [postFormData, setPostFormData] = useState({})
  const [idToUpdate, setIdToUpdate] = useState(0)
  const [patchFormData, setPatchFormData] = useState({})
  const [users, setUsers] = useState([])
  const [search, setSearch] = useState('')

  // http://127.0.0.1:7000

  useEffect(() => {
    fetch('/countries')
    .then(response => response.json())
    .then(countryData => setCountries(countryData))
  }, [])

  useEffect(() => {
    fetch('/trips')
    .then(response => response.json())
    .then(tripData => setTrips(tripData))
  }, [])

  useEffect(() => {
    if(trips.length > 0 && trips[0].id){
      setIdToUpdate(trips[0].id)
    }
  }, [trips])

  useEffect(() => {
    fetch('/users')
    .then(response => response.json())
    .then(userData => setUsers(userData))
  }, [])

  function addTrip(event){
    event.preventDefault()

    fetch('/trips', {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(postFormData)
    })
    .then(response => response.json())
    .then(newTrip => setTrips(trips => [...trips, newTrip]))
  }

  function updateTrip(event){
    event.preventDefault()
    fetch(`/trips/${idToUpdate}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(patchFormData)
    })
    .then(response => response.json())
    .then(updatedTrip => {
      setTrips(trips => {
        return trips.map(trip => {
          if(trip.id === updatedTrip.id){
            return updatedTrip
          }
          else{
            return trip
          }
        })
      })
    })
  }

  function deleteTrip(id){
    fetch(`/trips/${id}`, {
      method: "DELETE"
    })
    .then(() => setTrips(trips => {
      return trips.filter(trip => {
        return trip.id !== id
      })
    }))
  }

function searchCountry(e) {
    setSearch(e.target.value)
}

const filterCountry = countries.filter(country => {
    if (search ==='') {
        return true
    }
    return country.country_name.toLowerCase().includes(search.toLowerCase())
})

  function updatePostFormData(event){
    setPostFormData({...postFormData, [event.target.name]: event.target.value})
  }

  function updatePatchFormData(event){
    setPatchFormData({...patchFormData, [event.target.name]: event.target.value})
  }

  return (
    <div className="app">
      <NavBar/>
      <Header />
      <Switch>
        <Route exact path="/">
          <h1>Welcome! Here is the list of Trips:</h1>
          <Search search = {search} setSearch = {setSearch} searchCountry = {searchCountry}/>
          <CountryList countries={filterCountry}/>
        </Route>
        <Route path="/add_trip">
          <NewTripForm users = {users} addTrip={addTrip} updatePostFormData={updatePostFormData}/>
        </Route>
        <Route path="/update_trip">
          <UpdateTripForm updateTrip={updateTrip} setIdToUpdate={setIdToUpdate} updatePatchFormData={updatePatchFormData} trips={trips}/>
        </Route>
        <Route>
          <Search search = {search} setSearch = {setSearch} searchCountry = {searchCountry}/>
          <CountryList countries={filterCountry}/>
        </Route>
      </Switch>
    </div>
  );
}

export default App;
