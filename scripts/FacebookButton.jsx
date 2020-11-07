import * as React from 'react';
import FacebookLogin from 'react-facebook-login/dist/facebook-login-render-props';
import { Socket } from './Socket';

function handleSubmit(response) {
  const { name } = response;
  const { email } = response;
  const profilePic = response.picture.data.url;

  Socket.emit('new facebook user', {
    name,
    email,
    profile_pic: profilePic,
  });
}

export default function FacebookButton() {
  return (
    <FacebookLogin
      appId="358098632282607"
      autoLoad={false}
      fields="name,email,picture"
      callback={handleSubmit}
      render={(renderProps) => (
        <button type="button" className="facebook-button" onClick={renderProps.onClick}>
          Login with Facebook
        </button>
      )}
    />
  );
}
