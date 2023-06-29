import {useState} from 'react'

function UpdateTripForm({updateTrip, setIdToUpdate, updatePatchFormData, trips}){

    const [updateFormSubmitted, setUpdateFormSubmitted] = useState(false)

    return (
        <div className="trip-form">
            <h2>Update Trip Form</h2>
            {updateFormSubmitted ? <h1>Trip Updated!</h1> :
            <form onSubmit={event => {
                updateTrip(event)
                setUpdateFormSubmitted(updateFormSubmitted => !updateFormSubmitted)
            }}>
                <label>Choose a Trip: </label>
                <select onChange={(event) => {
                    setIdToUpdate(event.target.value)
                }} name="id">
                {trips.map(trip => {
                    return <option key={trip.id} value={trip.id}>{`${trip.id}: ${trip.name}`}</option>
                })}
                </select>
                <input onChange={updatePatchFormData} type="text" name="name" placeholder="Country name"/>
                <input onChange={updatePatchFormData} type="text" name="date" placeholder="Date / Time"/>
                <input type="submit" value="Update Trip"/>
            </form>}
        </div>
    )
}

export default UpdateTripForm