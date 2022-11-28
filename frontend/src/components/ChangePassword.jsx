import React from "react";
import {
  Button,
  DialogTitle,
  DialogContent,
  TextField,
  DialogActions,
  FormControl,
  IconButton,
  InputAdornment,
} from "@mui/material";
import Visibility from "@mui/icons-material/Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";
import crypto from "crypto-js";

export default function ChangePassword({ submit }) {
  const [currPass, setCurrPass] = React.useState("");
  const [newPass, setNewPass] = React.useState("");

  const [confirmNewPass, setConfirmNewPass] = React.useState("");
  const [matchingPassErr, setMatchingPassErr] = React.useState(false);
  const [passwordErr, setPasswordErr] = React.useState(false);
  const [showNew, setShowNew] = React.useState(false);
  const [showConfirm, setShowConfirm] = React.useState(false);

  const titleStyle = { margin: "5px 5px" };
  const buttonStyle = { margin: "10px" };

  const handleShowNew = () => {
    const newVisibility = !showNew;
    setShowNew(newVisibility);
  };
  const handleShowConfirm = () => {
    const confirmVisibility = !showConfirm;
    setShowConfirm(confirmVisibility);
  };
  // check that new and confirm new passwords are valid
  const checkValidPasswordsErr = (password) => {
    const uppercaseRegExp = /(?=.*?[A-Z])/;
    const lowercaseRegExp = /(?=.*?[a-z])/;
    const digitsRegExp = /(?=.*?[0-9])/;
    const specialCharRegExp = /(?=.*?[#?!@$%^&*-])/;

    if (
      password.length < 8 ||
      !uppercaseRegExp.test(password) ||
      !lowercaseRegExp.test(password) ||
      !digitsRegExp.test(password) ||
      !specialCharRegExp.test(password)
    ) {
      setPasswordErr(true);
    } else {
      setPasswordErr(false);
    }
  };

  // check that new and confirm new passwords match
  const checkConfirmPasswordErr = () => {
    // passwords dont match
    if (newPass === confirmNewPass) {
      // error
      setMatchingPassErr(false);
      return false;
    } else {
      setMatchingPassErr(true);
      return true;
    }
  };

  const handleChangePassword = () => {
    if (
      checkConfirmPasswordErr() ||
      checkValidPasswordsErr(newPass) ||
      checkValidPasswordsErr(confirmNewPass)
    ) {
      return false;
    } else {
      const hashedcurrpass = crypto.SHA3(currPass).toString();
      const hashednewpass = crypto.SHA3(newPass).toString();
      submit(hashedcurrpass, hashednewpass);
      return true;
    }
  };

  return (
    <>
      <DialogTitle style={titleStyle}>Change Password</DialogTitle>
      <DialogContent>
        <FormControl>
          <TextField
            required
            label="Current Password"
            type="text"
            variant="outlined"
            onChange={(e) => {
              setCurrPass(e.target.value);
            }}
          />
        </FormControl>
      </DialogContent>
      <DialogContent>
        <FormControl>
          <TextField
            required
            label="New Password"
            // type="text"
            variant="outlined"
            onChange={(e) => {
              setNewPass(e.target.value);
            }}
            helperText={
              matchingPassErr || passwordErr
                ? "invalid password or not matching"
                : ""
            }
            error={matchingPassErr || passwordErr ? true : false}
            type={showNew ? "text" : "password"}
            InputProps={{
              endAdornment: (
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    onClick={handleShowNew}
                  >
                    {showNew ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              ),
            }}
          />
        </FormControl>
      </DialogContent>
      <DialogContent>
        <FormControl>
          <TextField
            required
            label="Confirm New Password"
            variant="outlined"
            onChange={(e) => {
              setConfirmNewPass(e.target.value);
            }}
            helperText={
              matchingPassErr || passwordErr
                ? "invalid password or not matching"
                : ""
            }
            error={matchingPassErr || passwordErr ? true : false}
            type={showConfirm ? "text" : "password"}
            InputProps={{
              endAdornment: (
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    onClick={handleShowConfirm}
                  >
                    {showConfirm ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              ),
            }}
          />
        </FormControl>
      </DialogContent>
      <DialogActions>
        <Button
          style={buttonStyle}
          variant="contained"
          onClick={handleChangePassword}
        >
          Change Password
        </Button>
      </DialogActions>
    </>
  );
}
