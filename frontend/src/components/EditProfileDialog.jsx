import React from "react";
import PropTypes from "prop-types";
import {
  Button,
  DialogTitle,
  DialogContent,
  TextField,
  DialogActions,
  FormControl,
} from "@mui/material";

export default function EditProfileDialog({ currInfo, submit }) {
  const [name, setName] = React.useState(currInfo.name);
  const [title, setTitle] = React.useState(currInfo.title);
  const [bio, setBio] = React.useState(currInfo.bio);

  const [nameError, setNameError] = React.useState(false);
  const [titleError, setTitleError] = React.useState(false);
  const [bioError, setBioError] = React.useState(false);

  const [hasAttemptedEdit, setHasAttemptedEdit] = React.useState(false);

  const checkValidity = () => {
    if (hasAttemptedEdit) {
      setTimeout(() => {
        checkNameValid();
        checkTitleValid();
        checkBioValid();
      }, 800);
    }
  };

  const checkNameValid = () => {
    // username must be between 2 and 20 characters long
    // using alpha characters only + spaces
    if (
      name.match(/^[a-zA-Z\s]*$/) === null ||
      name.length < 2 ||
      name.length > 20
    ) {
      setNameError(true);
      return true;
    } else {
      setNameError(false);
      return false;
    }
  };

  const checkTitleValid = () => {
    // title must be less than 20 characters long
    if (title.length > 20) {
      setTitleError(true);
      return true;
    } else {
      setTitleError(false);
      return false;
    }
  };

  const checkBioValid = () => {
    // bio must be less than 200 characters long
    if (bio.length > 200) {
      setBioError(true);
      return true;
    } else {
      setBioError(false);
      return false;
    }
  };

  const handleEditSubmit = () => {
    setHasAttemptedEdit(true);
    if (checkNameValid() || checkTitleValid() || checkBioValid()) {
      alert("please check all errors");
    } else {
      submit(name, title, bio);
    }
  };

  const titleStyle = { margin: "20px 5px" };
  const formStyle = { display: "flex", margin: "0px" };
  const firstInputStyle = { width: "100%", marginTop: "15px" };
  const inputStyle = { width: "100%" };
  const buttonStyle = { margin: "10px" };

  return (
    <>
      <DialogTitle style={titleStyle}>Edit Profile</DialogTitle>
      <DialogContent style={formStyle}>
        <FormControl style={firstInputStyle}>
          <TextField
            id="edit-name"
            label="Name"
            aria-label="name"
            type="name"
            variant="outlined"
            defaultValue={currInfo.name}
            onBlur={checkValidity}
            onChange={(e) => {
              setName(e.target.value);
            }}
            helperText={
              nameError
                ? "please enter a name between 2 and 20 characters long using letters and spaces only"
                : ""
            }
            error={nameError ? true : false}
          />
        </FormControl>
      </DialogContent>
      <DialogContent style={formStyle}>
        <FormControl style={inputStyle}>
          <TextField
            id="edit-title"
            label="Title"
            aria-label="title"
            type="text"
            variant="outlined"
            defaultValue={currInfo.title}
            onBlur={checkValidity}
            onChange={(e) => {
              setTitle(e.target.value);
            }}
            helperText={
              titleError
                ? "please enter a title less than 20 characters long"
                : ""
            }
            error={titleError ? true : false}
          />
        </FormControl>
      </DialogContent>
      <DialogContent style={formStyle}>
        <FormControl style={inputStyle}>
          <TextField
            id="edit-bio"
            label="Bio"
            aria-label="bio"
            type="text"
            variant="outlined"
            defaultValue={currInfo.bio}
            onBlur={checkValidity}
            onChange={(e) => {
              setBio(e.target.value);
            }}
            helperText={
              bioError ? "please enter a bio less than 200 characters long" : ""
            }
            error={bioError ? true : false}
          />
        </FormControl>
      </DialogContent>
      <DialogActions>
        <Button
          style={buttonStyle}
          variant="contained"
          onClick={handleEditSubmit}
        >
          Submit
        </Button>
      </DialogActions>
    </>
  );
}

EditProfileDialog.propTypes = {
  submit: PropTypes.array,
  currInfo: PropTypes.array,
};
