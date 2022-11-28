import React from "react";
import {
  Box,
  Button,
  TextField,
  FormControl,
  IconButton,
  Typography,
} from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";
import DoneIcon from "@mui/icons-material/Done";

export default function RecipeAddSteps({
  formData,
  setFormData,
  validateData,
}) {
  const [recipeSteps, setRecipeSteps] = React.useState("");
  const [recipeStepError, setRecipeStepError] = React.useState(false);
  const [disabled, setDisable] = React.useState(
    Array(formData.steps.length).fill(true)
  );
  const [recipeStepArray, setRecipeStepArray] = React.useState(formData.steps);
  const [overallError, setOverallError] = React.useState(false);

  React.useEffect(() => {
    if (validateData === true) {
      if (formData.steps.length === 0) {
        setOverallError(true);
      } else {
        setOverallError(false);
      }
    }
  }, [validateData, formData.steps.length]);

  const addStep = () => {
    if (recipeSteps) {
      let list = formData.steps;
      list.push(recipeSteps);
      setFormData({ ...formData, steps: list });
      setRecipeStepArray(list);
      let disabledList = disabled;
      disabledList.push(true);
      setDisable(disabledList);
    } else {
      setRecipeStepError(true);
    }
    setRecipeSteps("");
    if (overallError) {
      setOverallError(false);
    }
  };

  const deleteRow = (index) => {
    const stepsList = formData.steps;
    stepsList.splice(index, 1);
    setFormData({ ...formData, steps: stepsList });
    setRecipeStepArray(stepsList);

    let disabledList = disabled;
    disabledList.splice(index, 1);
    setDisable(disabledList);
  };

  const editRow = (index) => {
    const updatedDisabled = [...disabled];
    updatedDisabled[index] = !updatedDisabled[index];
    setDisable(updatedDisabled);
  };

  const handleChangeRow = (e, index) => {
    const listSteps = [...recipeStepArray];
    listSteps[index] = e;
    setRecipeStepArray(listSteps);
    setFormData({ ...formData, steps: listSteps });
  };

  const divStyle = {
    display: "grid",
    alignItems: "start",
    marginBottom: "30px",
  };
  const labelStyle = { textAlign: "left" };
  const recipeStepStyle = { textAlign: "left" };
  const submitButtonStyle = {
    marginLeft: "auto",
    marginRight: "30px",
    width: "150px",
    minHeight: "50px",
    display: "flex",
    flexDirection: "row",
  };
  const iconStyle = { float: "right" };
  const stepStyle = { width: "90%" };
  const helperText = {
    textAlign: "left",
    letterSpacing: "0.03333em",
    fontFamily: "Arial",
    color: "#d4323e",
    fontSize: "0.75rem",
  };

  return (
    <>
      <Box style={divStyle}>
        <Typography variant="h5" style={labelStyle}>
          Add a Step
        </Typography>
        <FormControl>
          <TextField
            required
            id="step-recipe"
            label="Step Description"
            aria-label="step"
            type="text"
            variant="outlined"
            defaultValue={recipeSteps}
            value={recipeSteps}
            multiline
            rows={3}
            style={{ marginBottom: "20px" }}
            onChange={(e) => {
              setRecipeSteps(e.target.value);
            }}
            error={recipeStepError}
            helperText={recipeStepError ? "Please add a step." : " "}
          />
          <Button
            variant="contained"
            aria-label="add-step-button"
            id="add-step"
            style={submitButtonStyle}
            onClick={() => addStep()}
          >
            Add Step
          </Button>
        </FormControl>
      </Box>

      <Box style={divStyle}>
        <Typography variant="h5" style={labelStyle}>
          Recipe Steps
        </Typography>
        <Typography style={helperText}>
          {overallError ? "Please add at least one step" : ""}
        </Typography>
        {recipeStepArray.map((option, index) => (
          <div key={index}>
            <Box sx={recipeStepStyle}>
              <Typography variant="h6" style={labelStyle}>
                Step {index + 1}
              </Typography>
              <IconButton
                sx={iconStyle}
                aria-label="delete"
                onClick={() => deleteRow(index)}
              >
                <DeleteIcon />
              </IconButton>
              <IconButton
                sx={iconStyle}
                aria-label="edit"
                onClick={() => editRow(index)}
              >
                {disabled[index] ? <EditIcon /> : <DoneIcon />}
              </IconButton>
              <TextField
                id="step-recipe"
                aria-label="step"
                type="text"
                variant="outlined"
                value={option}
                multiline
                disabled={disabled[index]}
                rows={3}
                style={{ marginBottom: "20px" }}
                onChange={(e) => {
                  handleChangeRow(e.target.value, index);
                }}
                error={recipeStepError}
                helperText={recipeStepError ? "Empty field!" : " "}
                sx={stepStyle}
              />
            </Box>
          </div>
        ))}
      </Box>

      <br />
    </>
  );
}
