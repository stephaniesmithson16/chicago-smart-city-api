import { useEffect, useState } from "react";

import "./App.css";

const PAGE_SIZE = 25;

function formatRisk(risk: string) {
  return risk.match(/\(([^)]+)\)/)?.[1] ?? risk;
}

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
        <div className="table-container">
        <table
          style={{
            borderCollapse: "separate",
            borderColor: "#ddd",
            width: "100%",
            marginTop: "2rem",
          }}
        >
          <colgroup>
            <col className="name-column" />
            <col />
            <col />
            <col />
            <col />
            <col />
            <col />
            <col />
            <col className="date-column" />
            <col className="violations-column" />
          </colgroup>
          <thead>
            <tr>
              <th className="name-cell">Name</th>
              <th>License</th>
              <th>Facility Type</th>
              <th>Address</th>
              <th>Zip</th>
              <th>Risk</th>
              <th>Result</th>
              <th>Type</th>
              <th className="date-cell">Date</th>
              <th>Violations</th>
            </tr>

          </thead>

          <tbody>
            {inspections.map((inspection) => (
              <tr key={inspection.inspection_id}>
                <td className="name-cell">{inspection.name}</td>
                <td>{inspection.license}</td>
                <td>{inspection.facility_type}</td>
                <td>{inspection.address}</td>
                <td>{inspection.zip_code}</td>
                <td>{formatRisk(inspection.risk)}</td>
                <td>{inspection.results}</td>
                <td>{inspection.inspection_type}</td>
                <td className="date-cell">{inspection.inspection_date}</td>
                <td className="violations-cell">
                  <div className="violations-preview">
                    {inspection.violations || "No violations"}
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        </div>
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
