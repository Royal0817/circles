import React from 'react'
import { useAuth0 } from '@auth0/auth0-react'


const Profile = () => {
    const { user, isAuthenticated } = useAuth0();
    return (
      isAuthenticated &&
      <div className='profile'>
        <img src={user.picture} alt={user.name}/>
        <h3> Welcome {user.name}</h3>
       
    </div>
  )
}

export default Profile