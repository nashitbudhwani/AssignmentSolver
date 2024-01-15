import React, { useRef } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Button from "@mui/material/Button";

function UploadButton({ icon, onPostIdUpdate, onFileSelect }) {
  const fileInputRef = useRef();

  const handleButtonClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    console.log(file);

    // Update the file state using onFileSelect callback
    if (onFileSelect) {
      onFileSelect(file);
    }
  };

  return (
    <>
      <Button
        variant="contained"
        color="primary"
        sx={{
          backgroundColor: "#78909c",
          transition: "background-color 0.3s",
          "&:hover": {
            backgroundColor: "#546e7a",
          },
          // Adjust the padding and fontSize according to your requirements
          p: "20px",
          fontSize: "1.5rem",
        }}
        onClick={handleButtonClick}
      >
        <FontAwesomeIcon icon={icon} style={{ marginRight: "10px", fontSize: '2em', color:'#fff'}} />
        Upload File
      </Button>
      <input
        type="file"
        style={{ display: "none" }}
        ref={fileInputRef}
        onChange={handleFileChange}
        accept="/*"
      />
    </>
  );
}

export default UploadButton;
