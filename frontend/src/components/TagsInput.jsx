import React from "react";
import { Chip, TextField } from "@mui/material";
import Downshift from "downshift";

// Note this implementation was inspired by:
// https://codesandbox.io/s/material-ui-input-with-chips-0s2j4?from-embed
export default function TagsInput({ ...props }) {
  const { placeholder, formData, setFormData, ...other } = props;
  const [inputValue, setInputValue] = React.useState("");
  const [selectedItem, setSelectedItem] = React.useState(formData.utensils);

  React.useEffect(() => {
    setFormData({ ...formData, utensils: selectedItem });
  }, [selectedItem, formData, setFormData]);

  function handleKeyDown(event) {
    if (event.key === "Enter") {
      const newSelectedItem = [...selectedItem];
      const duplicatedValues = newSelectedItem.indexOf(
        event.target.value.trim()
      );

      if (duplicatedValues !== -1) {
        setInputValue("");
        return;
      }
      if (!event.target.value.replace(/\s/g, "").length) return;

      const newItem = event.target.value.trim();
      const newItemCapital = newItem.charAt(0).toUpperCase() + newItem.slice(1);

      newSelectedItem.push(newItemCapital);
      setSelectedItem(newSelectedItem);
      setInputValue("");
      setFormData({ ...formData, utensils: newSelectedItem });
    }
    if (
      selectedItem.length &&
      !inputValue.length &&
      event.key === "Backspace"
    ) {
      setSelectedItem(selectedItem.slice(0, selectedItem.length - 1));
      setFormData({ ...formData, utensils: selectedItem });
    }
  }
  function handleChange(item) {
    let newSelectedItem = [...selectedItem];
    if (newSelectedItem.indexOf(item) === -1) {
      newSelectedItem = [...newSelectedItem, item];
    }
    setInputValue("");
    setSelectedItem(newSelectedItem);
    setFormData({ ...formData, utensils: newSelectedItem });
  }

  const handleDelete = (item) => () => {
    const newSelectedItem = [...selectedItem];
    newSelectedItem.splice(newSelectedItem.indexOf(item), 1);
    setSelectedItem(newSelectedItem);
    setFormData({ ...formData, utensils: newSelectedItem });
  };

  function handleInputChange(event) {
    setInputValue(event.target.value);
  }
  return (
    <React.Fragment>
      <Downshift
        id="downshift-multiple"
        inputValue={inputValue}
        onChange={handleChange}
        selectedItem={selectedItem}
      >
        {({ getInputProps }) => {
          const { onBlur, onChange, onFocus, ...inputProps } = getInputProps({
            onKeyDown: handleKeyDown,
            placeholder,
          });
          return (
            <div>
              <TextField
                InputProps={{
                  startAdornment: selectedItem.map((item) => (
                    <Chip
                      key={item}
                      tabIndex={-1}
                      label={item}
                      sx={{ marginRight: "10px" }}
                      onDelete={handleDelete(item)}
                    />
                  )),
                  onBlur,
                  onChange: (event) => {
                    handleInputChange(event);
                    onChange(event);
                  },
                  onFocus,
                }}
                {...other}
                {...inputProps}
              />
            </div>
          );
        }}
      </Downshift>
    </React.Fragment>
  );
}
