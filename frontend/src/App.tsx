import { useEffect, useState } from "react";

const PAGE_SIZE = 25;

type Inspection = {
  inspection_id: number;
  name: string;
  aka_name: string;
  license: string;
  facility_type: string;
  address: string;
  zip_code: string;
  risk: string;
  results: string;
  inspection_date: string;
  inspection_type: string;
  violations: string;
};

function App() {
  const [inspections, setInspections] = useState<Inspection[]>([]);
  const [loading, setLoading] = useState(true);
  const [offset, setOffset] = useState<number>(0);

  useEffect(() => {
    async function fetchInspections() {
      try {
        setLoading(true);

        const response = await fetch(
          `http://127.0.0.1:8000/api/v1/restaurants/inspections?limit=${PAGE_SIZE}&offset=${offset}`,
        );

        const data = await response.json();

        setInspections(data);
      } catch (error) {
        console.error("Failed to fetch inspections:", error);
      } finally {
        setLoading(false);
      }
    }

    fetchInspections();
  }, [offset]);

  return (
    <main
      style={{ padding: "2rem", fontFamily: "sans-serif", fontSize: "16px" }}
    >
      <h1>Chicago Restaurant Inspections</h1>

      {loading ? (
        <p>Loading inspections...</p>
      ) : (
        <table
          style={{
            borderCollapse: "separate",
            borderColor: "#ddd",
            width: "100%",
            marginTop: "2rem",
          }}
        >
          <thead>
            <tr>
              <th>Name</th>
              <th>Aka Name</th>
              <th>License</th>
              <th>Facility Type</th>
              <th>Address</th>
              <th>Zip</th>
              <th>Risk</th>
              <th>Result</th>
              <th>Type</th>
              <th>Date</th>
            </tr>
          </thead>

          <tbody>
            {inspections.map((inspection) => (
              <tr key={inspection.inspection_id}>
                <td>{inspection.name}</td>
                <td>{inspection.aka_name}</td>
                <td>{inspection.license}</td>
                <td>{inspection.facility_type}</td>
                <td>{inspection.address}</td>
                <td>{inspection.zip_code}</td>
                <td>{inspection.risk}</td>
                <td>{inspection.results}</td>
                <td>{inspection.inspection_type}</td>
                <td>{inspection.inspection_date}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
      <div style={{ display: "flex",
        alignItems: "center",
        justifyContent: "center",
        marginTop: "2rem",
        gap: "2rem"}}>
        <button
          style={{
            padding: "0.5rem 1rem",
            fontSize: "16px",
            cursor: "pointer",
          }}
          onClick={() => {
            setOffset((currentOffset) => Math.max(currentOffset - PAGE_SIZE, 0));
          }}
          disabled={offset === 0}
        >
          Back
        </button>
        <button
          style={{
            padding: "0.5rem 1rem",
            fontSize: "16px",
            cursor: "pointer",
          }}
          onClick={() => {
            setOffset((currentOffset) => currentOffset + PAGE_SIZE);
          }}
        >
          Next
        </button>
      </div>
    </main>
  );
}

export default App;
