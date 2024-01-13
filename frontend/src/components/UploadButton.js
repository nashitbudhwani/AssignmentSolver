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
        variant="none"
        color="normal"
        sx={{
          m: 0,
          px: "550px",
          py: "200px",
          backgroundColor: "#afc0c2",
          transition: "background-color 0.3s", // Optional: Add a transition for a smoother effect
          "&:hover": {
            backgroundColor: "#78909c", // Change the background color on hover
          },
        }}
        onClick={handleButtonClick}
      >
        <FontAwesomeIcon icon={icon} style={{ marginRight: "10px", fontSize: '5em', color:'#8f826d'}} />
        {/* Adjust the width and fontSize according to your requirements */}
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
