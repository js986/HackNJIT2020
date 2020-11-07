import * as React from 'react';
import { GoogleLogin } from 'react-google-login';
import { Socket } from './Socket';

function handleSubmit(response) {
  const { name } = response.profileObj;
  const { email } = response.profileObj;
  const profilePic = response.profileObj.imageUrl;
  Socket.emit('new google user', {
    name,
    email,
    profile_pic: profilePic,
  });
}

export default function GoogleButton() {
  return (
    <GoogleLogin
      clientId="111391280363-q6etlte5rb97bsamdt5kfpre52cd5iri.apps.googleusercontent.com"
      onSuccess={handleSubmit}
      onFailure={handleSubmit}
      buttonText="Login with Google"
      icon
      cookiePolicy="single_host_origin"
    />
  );
}
