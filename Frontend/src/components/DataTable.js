import React, {useState,useEffect} from "react";
import axios from "axios";

const DataTable = () =>{
    const [dataFiles, setDataFiles] = useState([]);

    useEffect(()=>{
        const fetchDataFiles = async () => {
            try {
                const response = await axios.get('/api/list/');
                setDataFiles(response.data);
            }catch (error) {
                console.error('Error fetching data files:', error);
            }
        };
        fetchDataFiles();
    },[]);
    return (
        <table>
            <thead>
                <tr>
                    <th>File</th>
                    <th>Processed</th>
                    <th>DataTypes</th>
                </tr>
            </thead>
            <tbody>
            {dataFiles.map((dataFile) => (
                <tr key={dataFile.id}>
                    <td>{dataFile.file.split('/').pop()}</td>
                    <td>{dataFile.processed ? 'Yes':'No'}</td>
                    <td>
                        {dataFile.data_types ? (
                            <ul>
                                {Object.entries(dataFile.data_types).map(([column,dtype]) =>(
                                    <li key={column}>{column}: {dtype}</li>
                                    ))}
                            </ul>
                        ):(
                            'N/A'
                        )}
                    </td>
                </tr>
            ))}
            </tbody>
        </table>
    );
};

export default DataTable;