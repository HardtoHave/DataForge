import React from "react";
import Fileupload from "./components/Fileupload";
import DataTable from "./components/DataTable";

const App = () =>{
    return (
        <div>
            <h1>Data Type Inference and Conversion</h1>
            <Fileupload/>
            <DataTable/>
        </div>
    );
};
export default App;